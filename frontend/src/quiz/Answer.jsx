import React, { useEffect, useState } from 'react'
import axios from 'axios'
import './Answer.css'
export default function Answer() {
  const [questions, setquestions] = useState([])

  const fetchQuestion = async ()=>{
    try{
      const res = await axios.get("http://127.0.0.1:8000/qrl/")
      setquestions(res.data)
    } catch(err){
      console.error('ERROR',err);
    }
  }

  useEffect(()=>{
    fetchQuestion()
  },[])
  console.log(questions);
  return (
    <div className='container mt-5'>
      { questions && questions.map((question, q_id)=>(
        <>
         <p>Selected Option: {question.rqs[0].selected_option}</p>
        <h2>{question.question}</h2>
        <div className="row">
          <div className="col-md-6">
            { question.choices.slice(0, 2).map((option, op_id)=>(
              <div className={`option-box ${
                option.option === question.answer.answer ? (question.rqs[0].selected_option === question.answer.answer ? "right" : (option.option === question.answer.answer ? "right" : "") ): (question.rqs[0].selected_option !== option.option ? "" : "wrong" )
            }`}>
                {option.option}
              </div>
            ))}
          </div>
          <div className="col-md-6">
            { question.choices.slice(2).map((option, op_id)=>(
              <div className={`option-box ${
                option.option === question.answer.answer ? (question.rqs[0].selected_option === question.answer.answer ? "right" : (option.option === question.answer.answer ? "right" : "")  ): (question.rqs[0].selected_option !== option.option ? "" : "wrong" )
            }`}>
              {option.option}
            </div>
            ))}
          </div>
        </div>
        </>
      ))}
      
    </div>
  )
}

