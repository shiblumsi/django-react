import './App.css'
import Persons from './pages/Persons'
import 'bootstrap/dist/css/bootstrap.min.css';
import Signup from './pages/Signup';
import Login from './pages/Login';
import Question from './quiz/Question';
import QuestionCreateForm from './quiz/QuestionCreateForm';
import Quiz from './quiz/Quiz';
import Answer from './quiz/Answer';
import StudentSignupForm from './quiz/StudentSignupForm'
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div>
        <nav>
          <Link to="/studeentSignup">studeentSignup</Link>
        </nav>

        <Routes>
          <Route path="/" element={<Quiz />} />
          <Route path="/studeentSignup" element={<StudentSignupForm />} />
          <Route path="/answer" element={<Answer />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;