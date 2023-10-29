import { ImageUpload } from './home';
import { BrowserRouter as Router, Routes, Route }
    from 'react-router-dom';
import { Landing } from './landing';
import { Login } from './login';

function App() {
  return (
    <Router>
        <Routes>
            <Route exact path='' exact element={<Login />} />
            <Route exact path='/landing' exact element={<Landing />} />
            <Route exact path='/classification' exact element={<ImageUpload />} />
        </Routes>
        
    </Router>
);
}

export default App;
