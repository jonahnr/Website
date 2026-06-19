# Decision Workspace API Contract

Use this contract when replacing the localStorage prototype with real auth and persistence.

## Auth

All authenticated routes should receive the current user from the backend auth provider, not from frontend state.
Do not accept `role`, `organizationId`, or `userId` as trusted authority from the browser.

Recommended auth events:

- `POST /api/auth/signup`
  - Creates an auth user, organization, and first `org_admin` membership.
  - Body: `{ "organizationName": "...", "name": "...", "email": "...", "password": "..." }`
  - Response: `{ "user": {}, "organization": {}, "workspace": {} }`
- `GET /api/me`
  - Returns current user profile, memberships, and available organizations.
  - Response: `{ "user": {}, "memberships": [], "organizations": [] }`
- Password reset
  - Use Supabase Auth `resetPasswordForEmail` or equivalent provider flow.
  - Redirect back to `/decision-workspace/?auth=login`.
- Human verification
  - Prototype uses a simple required arithmetic check.
  - Production should use Cloudflare Turnstile, hCaptcha, or Supabase CAPTCHA verification on signup and login-sensitive actions.

## Workspace Read

- `GET /api/workspace/:organizationId`
  - Allowed roles: `parallax_admin`, active org member.
  - Response:

```json
{
  "organization": {},
  "users": [],
  "recommendations": [],
  "metrics": [],
  "decisions": [],
  "dashboards": []
}
```

Only return rows where `deleted_at is null`.

## Artifact Mutations

Use the same pattern for `recommendations`, `metrics`, `decisions`, and `dashboards`.

- `POST /api/:artifactType`
  - Allowed roles: `parallax_admin`, `org_admin`, `owner`, `contributor`.
  - Body must include `organizationId`.
  - Server verifies the user may edit that organization.
- `PATCH /api/:artifactType/:id`
  - Allowed roles: `parallax_admin`, `org_admin`, `owner`, `contributor`.
  - Server looks up the row and verifies organization access before update.
- `DELETE /api/:artifactType/:id`
  - Allowed roles: `parallax_admin`, `org_admin`, `owner`, `contributor`.
  - Soft delete by setting `deleted_at`.
  - Insert an `audit_events` row.

## User And Membership Admin

- `POST /api/orgs/:organizationId/users/invite`
  - Allowed roles: `parallax_admin`, `org_admin`.
  - Creates or links a user profile and membership.
- `PATCH /api/orgs/:organizationId/users/:userId`
  - Allowed roles: `parallax_admin`, `org_admin`.
  - Updates membership role or display profile details.
- `DELETE /api/orgs/:organizationId/users/:userId`
  - Allowed roles: `parallax_admin`, `org_admin`.
  - Soft deletes membership.
  - Must reject deleting the current user's own active membership unless another org admin remains.

## Organization Admin

- `GET /api/orgs`
  - `parallax_admin`: all active organizations.
  - org members: organizations where they have active membership.
- `DELETE /api/orgs/:organizationId`
  - Allowed roles: `parallax_admin` only.
  - Require two confirmations in the UI before calling this route.
  - Server should still require an explicit confirmation body:

```json
{
  "confirm": "DELETE Organization Name",
  "reason": "Client offboarding or mistaken test organization"
}
```

Server behavior:

- Verify `confirm` exactly matches the active organization name.
- Set `organizations.deleted_at`, `deleted_by`, and `deletion_reason`.
- Soft delete memberships and all organization artifacts.
- Insert one `audit_events` row with `event_type = "organization.deleted"`.
- Return the next accessible organization list.

## Frontend Replacement Points

Replace these local functions with async API calls:

- `loadData()` -> `GET /api/me` and `GET /api/workspace/:organizationId`
- `saveData()` -> remove; mutations should call API endpoints.
- `loadSession()` / `saveSession()` -> auth provider session.
- `handleLogin()` -> auth provider sign-in.
- `handleSignup()` -> `POST /api/auth/signup`.
- `handleItemSubmit()` -> artifact `POST` or `PATCH`.
- `deleteItem()` -> artifact `DELETE`.
- `deleteActiveOrg()` -> `DELETE /api/orgs/:organizationId`.

## Release Gate

Before inviting real clients:

- No passwords in frontend state or demo data.
- Server-side role checks on every route.
- Row-level security or equivalent database policy enabled.
- Organization deletion is soft-delete plus audit, not hard delete.
- Export route verifies organization access before rendering data.
