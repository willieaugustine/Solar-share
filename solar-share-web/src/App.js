import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import Profile from './components/Profile';
import Trade from './components/Trade';

const App = () => (
    <Router>
        <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/profile" component={Profile} />
            <Route path="/trade" component={Trade} />
        </Switch>
    </Router>
);

export default App;
