(function initializeDecisionWorkspaceSupabase() {
  "use strict";

  const SUPABASE_URL =
    "https://lyroglvvefeimjkddgtc.supabase.co";

  const SUPABASE_PUBLISHABLE_KEY =
    "sb_publishable_7cZGtPH-fRHH5EfiJoz2Wg_VsushoV1";

  if (!window.supabase?.createClient) {
    console.error("Supabase library did not load.");
    return;
  }

  const client = window.supabase.createClient(
    SUPABASE_URL,
    SUPABASE_PUBLISHABLE_KEY,
    {
      auth: {
        persistSession: true,
        autoRefreshToken: true,
        detectSessionInUrl: true
      }
    }
  );

  window.decisionWorkspaceSupabase = {
    client
  };

  console.log("Decision Workspace connected to Supabase.");
})();