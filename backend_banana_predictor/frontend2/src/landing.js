
import * as React from 'react';
import AspectRatio from '@mui/joy/AspectRatio';
import Button from '@mui/joy/Button';
import Card from '@mui/joy/Card';
import CardContent from '@mui/joy/CardContent';
import Typography from '@mui/joy/Typography';
import Grid from '@mui/joy/Grid';
import { CssVarsProvider, extendTheme } from '@mui/joy/styles';
import GlobalStyles from '@mui/joy/GlobalStyles';
import CardOverflow from '@mui/joy/CardOverflow';
import Divider from '@mui/joy/Divider';
import Chip from '@mui/joy/Chip';
import { useAuth0 } from "@auth0/auth0-react";
import Avatar from '@mui/joy/Avatar';
 
export const Landing = () => {
    const { user, loginWithRedirect, isAuthenticated, logout } = useAuth0();
    console.log("Current User", user);
    return (
        <CssVarsProvider defaultMode="dark">
            <GlobalStyles
            styles={{
            body: {
                padding: '8px',
                backgroundColor: '#272727',
                backgroundImage: 'url(https://images.unsplash.com/photo-1520658289427-977eb66c2dbd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2669&q=80)',
                backgroundSize: 'fill',
                overflowX: 'hidden',
                overflowY: 'auto',
                backgroundFilter: 'blur(100px)',
            },
            }}
        />
        <Grid container spacing={6}
        margin="auto">
        <Grid  xs={12} display="flex" justifyContent="center">
            <Typography level="h1" style={{ fontSize: '64px' }}>{''}
            <Typography variant="neutral" color="success">
            Crop
            </Typography>Tech AI
            </Typography>
            
        </Grid>
        { isAuthenticated &&
        <Grid  xs={12} display="flex" justifyContent="center" alignItems="center" >
            <Avatar sx={{ ml:2, mr:2}} alt="Avatar" src={user.picture} />
            <Typography level="h4">{user.name}</Typography>
            <Button sx={{ ml:2}}color="danger" variant="outlined" onClick={(e) => logout()}>Logout</Button>
        </Grid>
        }   
        <Grid container spacing={12} xs={12} display="flex" justifyContent="center">
        <Grid xs={3.5}>
            <Card variant="solid"
            color="outlined"
            invertedColors
            sx={{
                boxShadow: 'md',
                width: '100%',
                maxWidth: '100%',
                // to make the demo resizeable
                overflow: 'auto',
                resize: 'horizontal',
            }}>

            <CardOverflow>
                <AspectRatio ratio="2">
                <img
                    src="https://images.unsplash.com/photo-1566393028639-d108a42c46a7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2643&q=80"

                    loading="lazy"
                    alt=""
                />
                </AspectRatio>
            </CardOverflow>
            <CardContent orientation="horizontal">
                <div>
                <Typography fontSize="lg" fontWeight="lg">
                    Banana Detection
                </Typography>
                <Typography level="body-xs">Lorem Ipsum</Typography>
                </div>
                <Button
                variant="solid"
                size="md"
                color="success"
                aria-label="Explore Bahamas Islands"
                sx={{ ml: 'auto', alignSelf: 'center', fontWeight: 600 }}
                component="a" href="/"
                >
                Explore
                </Button>
            </CardContent>
            </Card>
        </Grid>
        <Grid xs={3.5}>
            <Card variant="solid"
            color="outlined"
            invertedColors
            sx={{
                boxShadow: 'md',
                width: '100%',
                maxWidth: '100%',
                // to make the demo resizeable
                overflow: 'auto',
                resize: 'horizontal',
            }}>
            <CardOverflow>
                <AspectRatio ratio="2">
                <img
                    src="https://img.emedihealth.com/wp-content/uploads/2023/02/ripe-or-unripe-banana-feat.jpg"
                    loading="lazy"
                    alt=""
                />
                </AspectRatio>
            </CardOverflow>
            <CardContent orientation="horizontal">
                <div>
                
                <Typography fontSize="lg" fontWeight="lg">
                    Banana Classification
                </Typography>
                <Typography level="body-xs">Lorem Ipsum</Typography>
                </div>
                <Button
                variant="solid"
                size="md"
                color="success"
                aria-label="Explore Bahamas Islands"
                sx={{ ml: 'auto', alignSelf: 'center', fontWeight: 600 }}
                component="a" href="/classification"
                >
                Explore
                </Button>
            </CardContent>
            </Card>
        </Grid>
        <Grid xs={3.5} 
        >
            <Card variant="solid"
            color="outlined"
            invertedColors
            sx={{
                boxShadow: 'md',
                width: '100%',
                maxWidth: '100%',
                // to make the demo resizeable
                overflow: 'auto',
                resize: 'horizontal',
            }}>

            <CardOverflow>
                <AspectRatio ratio="2">
                <img
                    src="https://images.unsplash.com/photo-1610989569524-40c18b22ace2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2576&q=80"
                    loading="lazy"
                    alt=""
                />
                </AspectRatio>
            </CardOverflow>
            <CardContent orientation="horizontal" >
                <div>
                
                <Typography fontSize="lg" fontWeight="lg">
                    Path Planning
                </Typography>
                <Typography level="body-xs">Lorem Ipsum</Typography>
                </div>
                <Button
                variant="solid"
                size="md"
                color="success"
                aria-label="Explore Bahamas Islands"
                sx={{ ml: 'auto', alignSelf: 'center', fontWeight: 600 }}
                component="a" href="/"
                >
                Explore
                </Button>
            </CardContent>
            </Card>
        </Grid>
        </Grid>
        
        <Grid  xs={12} display="flex" justifyContent="center">
            <Chip slotProps={{ action: { component: 'a', href: '#as-link' } }} color="neutral" size="lg" variant="solid">Made By Team Tripods</Chip>
        </Grid>
        <Grid  xs={12} display="flex" justifyContent="center">
            <Typography level="h4" >Made Using</Typography>
        </Grid>
        <Grid  container spacing={8} xs={12} display="flex" justifyContent="center" >
        <Grid  sx={{ maxWidth: 140}}>
            <img
                src="https://i.pinimg.com/originals/95/91/ed/9591ed82caa8d20c30db96cb7298d3a9.png"
                loading="lazy"
                alt=""
                width="100%"
                style={{ backgroundColor: '#fff', padding: 12, borderRadius: 8 }}
            />
        </Grid>
        <Grid  sx={{ maxWidth: 300}}>
            <img
                src="https://cdn.cookielaw.org/logos/70564414-548a-4286-8ad7-04d95b172a08/e26443c0-68d1-47c8-b8fc-9bc765da2e95/3a159462-db70-43cf-a27d-f602a6baed44/pm-logo-horiz.png"
                loading="lazy"
                alt=""
                width="100%"
                style={{ backgroundColor: '#fff', padding: 12, borderRadius: 8 }}
            />
        </Grid>
        <Grid  sx={{ maxWidth: 240}}>
            <img
                src="https://camo.githubusercontent.com/4079196b56fceacd94ff768d51a1b9b8f5ec11f31ab9a76d417be4b128e3c0cd/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6c65746563682d6469676974616c2d736f6c7574696f6e732f696d6167652f75706c6f61642f76313637343535343437332f47726f75705f3133315f6d636d6e32652e706e67"
                loading="lazy"
                alt=""
                width="100%"
            />
        </Grid>
        <Grid  sx={{ maxWidth: 240}}>
            <img
                src="https://www.pygame.org/docs/_images/pygame_powered.png"
                loading="lazy"
                alt=""
                width="100%"
                style={{ backgroundColor: '#fff', padding: 12, borderRadius: 8 }}
            />
        </Grid>
        <Grid  sx={{ maxWidth: 270}}>
            <img
                src="https://miro.medium.com/v2/resize:fit:521/0*ua4BvbPc6PYNHJUm"
                loading="lazy"
                alt=""
                width="100%"
                style={{borderRadius: 8 }}
            />
        </Grid>
        <Grid  sx={{ maxWidth: 250}}>
            <img
                src="https://miro.medium.com/v2/resize:fit:2000/0*NBHDwcLORYcBEsM1.jpg"
                loading="lazy"
                alt=""
                width="100%"
                style={{borderRadius: 8 }}
            />
        </Grid>
        <Grid  sx={{ maxWidth: 250}}>
            <img
                src="https://res.cloudinary.com/practicaldev/image/fetch/s--u9yx6diw--/c_imagga_scale,f_auto,fl_progressive,h_500,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/anuqor6vk1ibmhq8ntrf.png"
                loading="lazy"
                alt=""
                width="100%"
                style={{borderRadius: 8 }}
            />
        </Grid>
        </Grid>
        <Grid  xs={12} display="flex" justifyContent="center">
        
        </Grid>
        </Grid>
        </CssVarsProvider>
    );
};

export default Landing;