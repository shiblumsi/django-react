import React, { useEffect, useState } from 'react'
import axios from 'axios'
export default function Quiz() {
    const [questions, setQuestions] = useState([])
    const [currentQustionIndex,setCurrentQustionIndex] = useState(0)
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
        return <div>Data Comming...</div>;
      }

    const currentQuestion = questions[currentQustionIndex]

   


  return (
    <div>
       <h2>{currentQuestion && currentQuestion.question}</h2>
       {currentQuestion.choices.map((opt)=>(
        <li>{opt.option}</li>
        ))}
    </div>
  )
}
