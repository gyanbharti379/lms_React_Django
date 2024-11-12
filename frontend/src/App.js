import React from 'react';
import { createBrowserRouter, createRoutesFromElements, Route,RouterProvider } from 'react-router-dom';
import ReactDOM from 'react-dom/client';
import Layout from './Components/Layout';
import Home from './Components/Home/Home';
import About from './Components/About/About_us';
import Contact from './Components/Contact/Contact_us';
import LoginSignUp from './Components/LoginAndSignUp/LoginSignUp';
import Dashboard from './Components/UserDashboard/Dashboard';


function App() {  
   
          // let routes = useRoutes([
          //   { path: "/", element:<Layout />,
          //     children: [
          //       { 
          //         path: "", element: <Home />
          //       },
          //       {
          //         path: "login", element: <LoginSignUp />
          //       },
          //       {
          //         path: "about", element: <About />
          //       },
          //       {
          //         path: "contact", element: <Contact />
          //       }
                  
          //     ]},
          // ]);

          // return routes;

          const router = createBrowserRouter(
            createRoutesFromElements(
              <Route path="/" element={<Layout />}>
                <Route index element={<Home />} />
                <Route path="login" element={<LoginSignUp />} />
                <Route path="about" element={<About />} />
                <Route path="contact" element={<Contact />} />

                <Route path="dashboard" element={<Dashboard/>} />
                <Route path="profile" element={<Dashboard/>} />
                <Route path="incident" element={<Dashboard/>} />
                <Route path="logout" element={<LoginSignUp/>} />

              </Route>
            )
          );
          ReactDOM.createRoot(document.getElementById('root')).render(
            <React.StrictMode>
              <RouterProvider router={router} />
            </React.StrictMode>
          );

            
  
}

export default App;
