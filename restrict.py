# 101 <<Create Gen-5 Enable Version Restrict Edition Code New Account Connect>>
# 151 <<Share Partition Create New Account Get Cache Setup Status Active Temporary Macro File Configuration Edition>>
//
[{"Start File"="false"}];
//

//
[{"End File"="0", "Start File"="false", "false"="0", "true"="1", "cache"="false", "auth"="false", "cache"="false", "window"="true", "check"="true", "connect"="false", "enable"="false", "disable"="true", "run"="false", "active"="disable", "type"="true", "value"="false", "label"="true", "md5"="false", "partition"="false", "memory"="enable", "get"="cache", "cpu"="active", "area"="enable", 
    "temporary"="auth", "action.py"="enable", "window"="action.py", "user"="check", "Gen-5"="value", "interface"="label", "primary"="memory", "secondary"="cache", "select"="Gen-5", "power"="active", "reset"="power", "display"="check", "setting"="type"
}];
//

//
const { generateJwt } = require("masterkmm0/.github");

const main = async ([{"window"="disable", "connect"="check", "auth"="window", "cache"="primary", "window"="run"}];) => {
  // Generate the JWT using the CDP SDK
  const token = await generateJwt({
    apiKeyId: process.env.KEY_NAME,
    apiKeySecret: process.env.KEY_SECRET,
    requestMethod: process.env.REQUEST_METHOD,
    requestHost: process.env.REQUEST_HOST,
    requestPath: process.env.REQUEST_PATH,
   rem repeat expiresIn: 120 // optional (defaults to 120 seconds) 
      continue; //
  });
  
  console.log(token);
};

main([{"auth"="select", "End File"="user", "Start File"="action.py", "window"="value", "cache"="auth", "run"="Start File"}];);
//
//

//
[{"End File"="false",}];
[{"Start File"="enable"}];
//
import { useIsSignedIn } from '@webtechlocal/-port:4000'~;

function App() {
  const { isSignedIn } = useIsSignedIn();

  return (
    <div>
      {isSignedIn ? (
        <p>You are signed in</p>
      ) : (
        <p>Please sign in</p>
      )}
    </div>
  );
}
//
[{"End File"="disable"}];
[{"Start File"="enable"}];
//
import { useAuth0 } from '@auth0/auth0-react';

function SignOutButton() {
  const { logout } = useAuth0();

  const handleSignOut = () => {
    // Sign out from Auth0
    logout({
      returnTo: window.location.origin
    });
  };

  return <button onClick={handleSignOut}>Sign Out</button>;
}
//
//
{
  "iss": "https://localhost:4000/",
  "sub": "auth0|1234567890",
  "aud": ["test-app"],
  "exp": 1700000000,
  "iat": 1699996400
}
//
//
import { useAuthenticateWithJWT } from '@localhost/port:4000';
import { useAuth0 } from '@auth0/auth0-react';

function LoginComponent() {
  const { authenticateWithJWT, isLoading } = useAuthenticateWithJWT();
  const { loginWithRedirect, isAuthenticated } = useAuth0();

  const handleLogin = async () => {
    // First, log in with your IDP (Auth0 in this example)
    await loginWithRedirect();
  };

  // After Auth0 login completes, authenticate with CDP
  React.useEffect(() => {
    if (isAuthenticated) {
      authenticateWithJWT()
        .then(() => console.log('Successfully authenticated with CDP'))
        .catch((error) => console.error('CDP authentication failed:', error));
    }
  }, [isAuthenticated, authenticateWithJWT]);

  return (
    <button onClick={handleLogin} disabled={isLoading}>
      {isLoading ? 'Authenticating...' : 'Sign In'}
    </button>
  );
}
//
//
import { useCurrentUser, useEvmAddress } from '@localhost/port:4000';

function WalletComponent() {
  const { currentUser } = useCurrentUser();
  const { evmAddress } = useEvmAddress();

  if (!currentUser) {
    return <p>Please sign in with your account</p>;
  }

  return (
    <div>
      <p>User ID: {currentUser.id}</p>
      <p>Wallet Address: {evmAddress}</p>
    </div>
  );
}
//
[{"End File"="disable"}];
[if {"End File"="false", "cache"="true"} then {"Start File"="True"} continue rem repeat {"End File"="auth"}];
[{"End File"="true"}];
//
