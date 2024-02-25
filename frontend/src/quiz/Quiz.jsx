import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function Quiz() {
    const [questions, setQuestions] = useState([]);
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
    const [answer, setAnswer] = useState({});

    const navigate = useNavigate();
    
    const fetchQuestions = async () => {
        try {
            const res = await axios.get("http://127.0.0.1:8000/ql/");
            setQuestions(res.data);
        } catch (err){
            console.error("error",err);
        }
    };

    useEffect(() => {
        fetchQuestions();
    }, []);

    if (questions.length === 0) {
        return <div>Loading...</div>;
    }

    const currentQuestion = questions[currentQuestionIndex];

    const handleNext = () => {
        setCurrentQuestionIndex(prevIndex => prevIndex + 1);
    };

    const handlePrevious = () => {
        setCurrentQuestionIndex(prevIndex => prevIndex - 1);
    };

    const handleOptionChange = (q_id, o_id) => {
        setAnswer(prevAns => ({
            ...prevAns,
            [q_id]: o_id
        }));
    };
   
    const handleSubmit = async () => {
        console.log(answer);
        try {
            const res = await axios.post("http://127.0.0.1:8000/qr/", { question_options: answer });
            console.log(res.data);
            navigate('/answer');
        } catch (error){
            console.error("Error", error);
        }
    };

    return (
        <div className="container mt-5">
            <h2>{currentQuestion && currentQuestion.question}</h2>
            <div className="row">
                <div className="col-md-6">
                    {currentQuestion.choices.slice(0, 2).map((option, o_id) => (
                        <div className="form-check mb-3" key={o_id}>
                            <input
                                type="radio"
                                className="form-check-input"
                                name={`question_${currentQuestion.id}`}
                                id={option.id}
                                value={option.id}
                                onChange={() => handleOptionChange(currentQuestion.id, option.id)}
                            />
                            <label className="form-check-label" htmlFor={option.id}>{option.option}</label>
                        </div>
                    ))}
                </div>
                <div className="col-md-6">
                    {currentQuestion.choices.slice(2).map((option, o_id) => (
                        <div className="form-check mb-3" key={o_id}>
                            <input
                                type="radio"
                                className="form-check-input"
                                name={`question_${currentQuestion.id}`}
                                id={option.id}
                                value={option.id}
                                onChange={() => handleOptionChange(currentQuestion.id, option.id)}
                            />
                            <label className="form-check-label" htmlFor={option.id}>{option.option}</label>
                        </div>
                    ))}
                </div>
            </div>
            <div className="mt-3">
                <button className="btn btn-primary mr-2" onClick={handlePrevious} disabled={currentQuestionIndex === 0}>
                    Previous
                </button>
                {currentQuestionIndex === questions.length - 1 ? (
                    <button className="btn btn-success" onClick={handleSubmit}>Submit Quiz</button>
                ) : (
                    <button className="btn btn-primary" onClick={handleNext} disabled={currentQuestionIndex === questions.length - 1}>
                        Next
                    </button>
                )}
            </div>
        </div>
    );
}
