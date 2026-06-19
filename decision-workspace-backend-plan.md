# Parallax Decision Workspace Backend Plan

This workspace is currently a static prototype using `localStorage` and `sessionStorage`.
Before real client use, move authentication and persistence to a real backend.

## Recommended Production Stack

Best fast path:

- Supabase Auth for email/password, magic links, and organization invite flows.
- Postgres tables using the schema in `decision-workspace-schema.sql`.
- API payload and route behavior from `decision-workspace-api-contract.md`.
- Row-level security by organization membership.
- Parallax admin role for cross-org access.
- Static frontend hosted on Cloudflare Pages or the existing site host.

Alternative stack:

- Clerk or Auth0 for auth.
- Cloudflare D1 or Neon Postgres for persistence.
- Cloudflare Workers / Pages Functions for API routes.

## Required Production Concepts

Organizations:

- One account per client organization.
- A user may belong to one or more organizations over time.
- Parallax admin users can access every organization.

Roles:

- `parallax_admin`: access every organization and reset/demo/admin tools.
- `org_admin`: manage users and all workspace artifacts inside one organization.
- `owner`: edit assigned operational artifacts.
- `contributor`: edit workspace artifacts but not users.
- `viewer`: read-only leadership access.

Core tables:

- `organizations`
- `users`
- `organization_memberships`
- `recommendations`
- `metrics`
- `decisions`
- `dashboards`
- `audit_events`

## API Routes Needed

Minimum routes:

- `POST /api/auth/signup`
- `POST /api/orgs`
- `GET /api/orgs`
- `DELETE /api/orgs/:orgId`
- `GET /api/workspace/:orgId`
- `POST /api/recommendations`
- `PATCH /api/recommendations/:id`
- `DELETE /api/recommendations/:id`
- Same CRUD pattern for `metrics`, `decisions`, and `dashboards`
- `POST /api/orgs/:orgId/users/invite`
- `PATCH /api/orgs/:orgId/users/:userId`
- `DELETE /api/orgs/:orgId/users/:userId`

## Frontend Migration Notes

Current local methods to replace:

- `loadData()`
- `saveData()`
- `loadSession()`
- `saveSession()`
- `handleLogin()`
- `handleSignup()`
- `handleItemSubmit()`
- `deleteItem()`
- `deleteActiveOrg()`

Keep the current UI modules and replace the storage calls with async API calls.
After each mutation, re-fetch the active organization workspace.

## Security Requirements

- Never store real passwords in frontend code or local storage.
- Never expose client workspace data to another organization.
- Use row-level security or equivalent server-side authorization.
- Add audit logs for create, update, delete, invite, and role changes.
- Organization deletion must be Parallax-admin-only, double-confirmed in the UI, re-checked on the server, soft-deleted in the database, and audit logged.
- Mark `decision-workspace.html` as `noindex` until production auth is live.

## Deployment Gate

Do not invite real clients until all of these are true:

- Real authentication is active.
- Organization data is server-side.
- Viewer/editor/admin roles are enforced server-side.
- Deletions are soft-deleted or audit logged.
- Password reset or magic link flow exists.
- Exported artifacts do not expose another organization's data.
