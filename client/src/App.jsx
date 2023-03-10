import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'

function App() {

  return (
      <>
          <BrowserRouter>
              <Routes>
                  <Route path="/">
                      <Route path="login">
                          <Route path />
                      </Route>
                      <Route
                          index
                          element={isAuthenticated() ? <Landing /> : <Login />}
                      />
                      <Route path="register">
                        <Route path="worker" element={isAuthenticated() ? <WorkerHome /> : <WorkerRegister />}>

                        </Route>
                      </Route>
                      <Route
                          path="profile"
                          element={!isAuthenticated() ? <Login /> : <Profile />}
                      />
                      {/* <Route
                          path="home"
                          element={!isAuthenticated() ? <Login /> : <Home />}
                      />
                      <Route
                          path="update"
                          element={!isAuthenticated() ? <Login /> : <Update />}
                      />
                      <Route
                          path="newpost"
                          element={!isAuthenticated() ? <Login /> : <NewPost />}
                      />
                      <Route
                          path="search"
                          element={!isAuthenticated() ? <Login /> : <Search />}
                      />
                      <Route
                          path="register"
                          element={isAuthenticated() ? <Home /> : <Register />}
                      /> */}
                  </Route>
              </Routes>
          </BrowserRouter>
      </>
  );
}

export default App


