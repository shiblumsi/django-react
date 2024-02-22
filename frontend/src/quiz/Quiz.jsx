import React, { useEffect, useState } from 'react'
import axios from 'axios'
export default function Quiz() {
    const [questions, setQuestions] = useState([])
    const [currentQuestionIndex,setCurrentQuestionIndex] = useState(0)
    const [answer, setAnswer] = useState({})
    
    const fetchQuestions = async () =>{
        try {
            const res = await axios.get("http://127.0.0.1:8000/ql/")
            setQuestions(res.data)
        } catch (err){
            console.error("error",err);
        }
    }

    useEffect(()=>{
        fetchQuestions()
    }, []);

    if (questions.length === 0) {
        return <div>Data coming...</div>;
      }

    const currentQuestion = questions[currentQuestionIndex]

    const handleNext = ()=>{
      setCurrentQuestionIndex(
        (previousQuestionIndex) => previousQuestionIndex + 1
      );
    }

    const handlePrevious = ()=>{
      setCurrentQuestionIndex((previousQuestionIndex)=> previousQuestionIndex - 1 )
    }

    const handleOptionChange = (q_id, o_id) => {
     console.log(q_id,o_id);
     setAnswer(pAns=>({
      ...pAns,
      [q_id]:o_id
     }))
    };
   
    const handleSubmit = async ()=>{
      console.log(answer);
      try {
        const res = await axios.post("http://127.0.0.1:8000/qr/",{question_options:answer});
        console.log(res.data);
      } catch (error){
        console.error("Error",error)
      }
      

    }
    console.log(questions);

  return (
    <>
      <h2>{currentQuestion && currentQuestion.question}</h2>
      {currentQuestion.choices.map((option, o_id) => (
        <div key={o_id}>
          <input
            type="radio"
            name={`question_${currentQuestion.id}`}
            value={option.id}
            onChange={() =>
              handleOptionChange(currentQuestion.id, option.id)
            }
          />
          <label htmlFor={option.id}>{option.option}</label>
        </div>
      ))}
      <button onClick={handlePrevious} disabled={currentQuestionIndex === 0}>
        Previous
      </button>
      {currentQuestionIndex === questions.length - 1 ? (
        <button onClick={handleSubmit}>submit quiz</button>
      ) : (
        <button
          onClick={handleNext}
          disabled={currentQuestionIndex === questions.length - 1}
        >
          Next
        </button>
      )}
    </>
  );
}
