-- Parallax Decision Workspace production schema draft.
-- Designed for Postgres/Supabase-style deployment.

create table organizations (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  industry text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  deleted_at timestamptz,
  deleted_by uuid,
  deletion_reason text
);

create table users_profile (
  id uuid primary key,
  name text not null,
  email text not null unique,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create type workspace_role as enum (
  'parallax_admin',
  'org_admin',
  'owner',
  'contributor',
  'viewer'
);

create table organization_memberships (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id),
  user_id uuid not null references users_profile(id) on delete cascade,
  role workspace_role not null default 'viewer',
  created_at timestamptz not null default now(),
  deleted_at timestamptz,
  unique (organization_id, user_id)
);

create type work_priority as enum ('High', 'Medium', 'Low');
create type work_status as enum ('Not started', 'In progress', 'Blocked', 'Done');
create type work_effort as enum ('Small', 'Medium', 'Large');
create type trust_status as enum ('Trusted', 'Needs review', 'Disputed', 'Unknown');
create type dashboard_action as enum ('Keep', 'Fix', 'Merge', 'Retire');

create table recommendations (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id),
  title text not null,
  why text not null,
  owner_user_id uuid references users_profile(id),
  priority work_priority not null default 'Medium',
  effort work_effort not null default 'Medium',
  status work_status not null default 'Not started',
  due_date date,
  related text,
  evidence text,
  next_step text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  deleted_at timestamptz
);

create table metrics (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id),
  name text not null,
  definition text not null,
  owner_user_id uuid references users_profile(id),
  contributors text,
  source text,
  logic text,
  refresh text,
  decision_supported text,
  disputes text,
  trust trust_status not null default 'Unknown',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  deleted_at timestamptz
);

create table decisions (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id),
  name text not null,
  owner_user_id uuid references users_profile(id),
  cadence text,
  supporting_metrics text,
  decision_options text,
  decision_criteria text,
  selected_option text,
  trigger_threshold text,
  forum text,
  escalation_path text,
  current_friction text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  deleted_at timestamptz
);

create table dashboards (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id),
  name text not null,
  report_url text,
  audience text,
  owner_user_id uuid references users_profile(id),
  platform text,
  location text,
  purpose text,
  sources text,
  trust_score int check (trust_score between 1 and 5),
  issues text,
  action dashboard_action not null default 'Fix',
  priority work_priority not null default 'Medium',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  deleted_at timestamptz
);

create table audit_events (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid references organizations(id),
  actor_user_id uuid references users_profile(id),
  event_type text not null,
  entity_type text not null,
  entity_id uuid,
  payload jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create index organizations_active_idx on organizations(created_at desc) where deleted_at is null;
create index organization_memberships_org_idx on organization_memberships(organization_id) where deleted_at is null;
create index recommendations_org_idx on recommendations(organization_id) where deleted_at is null;
create index metrics_org_idx on metrics(organization_id) where deleted_at is null;
create index decisions_org_idx on decisions(organization_id) where deleted_at is null;
create index dashboards_org_idx on dashboards(organization_id) where deleted_at is null;
create index audit_events_org_idx on audit_events(organization_id, created_at desc);
