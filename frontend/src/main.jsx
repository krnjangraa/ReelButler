import React from 'react'

import ReactDOM from 'react-dom/client'

import {

  BrowserRouter,

  Routes,

  Route

} from 'react-router-dom'

import './index.css'

import Dashboard from './pages/Dashboard'

import CreatorStudio from './pages/CreatorStudio'

import TrendDetails from './pages/TrendDetails'


ReactDOM.createRoot(
  document.getElementById('root')
).render(

  <BrowserRouter>

    <Routes>

      <Route
        path="/"
        element={<Dashboard />}
      />

      <Route
        path="/video/:videoId"
        element={<TrendDetails />}
      />
      <Route
    path="/studio"
    element={<CreatorStudio />}
      />
    </Routes>

  </BrowserRouter>
)