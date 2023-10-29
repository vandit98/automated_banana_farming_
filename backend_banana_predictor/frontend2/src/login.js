import Button from '@mui/joy/Button';
import { CssVarsProvider, extendTheme } from '@mui/joy/styles';
import GlobalStyles from '@mui/joy/GlobalStyles';
import Box from '@mui/material/Box';
import { useAuth0 } from "@auth0/auth0-react";

export const Login = () => {
    const { user, loginWithRedirect } = useAuth0();
    return (
        <CssVarsProvider defaultMode="dark">
        <GlobalStyles
        styles={{
        body: {
            padding: '8px',
            backgroundColor: '#272727',
            margin: 'auto',
            position: 'absolute',
            top: '40%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            display: 'flex',
            flexDirection: 'row',
        },
        }}
    />
    <Box
     sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        p: 1,
        m: 1,
        bgcolor: 'background.paper',
        borderRadius: 1,
      }}
    >
        <img
            src="https://www.quintagroup.com/blog/blog-images/saml2/auth0.png/@@images/image.png"
            loading="lazy"
            alt=""
            width="20%"
            style={{ backgroundColor: '#fff', padding: 12, borderRadius: 8 }}
        />
    </Box>
    
    <Box
    sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        p: 1,
        m: 1,
        bgcolor: 'background.paper',
        borderRadius: 1,
      }}
    >

    
    <Button onClick={(e) => loginWithRedirect()}>Login with Redirect</Button>
    </Box>

    </CssVarsProvider>
    );
};