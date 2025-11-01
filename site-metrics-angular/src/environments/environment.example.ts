export const environment = {
  production: false,
  apiUrl: [
    'url to your development api',
  ],
  auth: {
    domain: '',
    clientId: '',
    audience: '',
    redirectUri: `${window.location.origin}/callback`,
    logoutUrl: `${window.location.origin}/`,
    returnTo: `${window.location.origin}/`
  }
};