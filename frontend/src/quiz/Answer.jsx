<<<<<<< HEAD
import React from 'react'

export default function Answer() {
  return (
    <div>
      
=======
import React, { useEffect ,useState} from 'react'
import axios from 'axios'
export default function Answer() {
    const [answers, setAnswers] = useState([])
    useEffect(()=>{
        const getResult = async ()=>{
            try{
            const res = await axios.get("http://127.0.0.1:8000/qrl/")
            setAnswers(res.data)
            } catch(err){
                console.error("error",err);
            }
        }
        
        getResult()
    },[])
    console.log(answers);
  return (
    <div>
        
>>>>>>> 724ca918379d3db470242400a6fd0c142d1f3b05
    </div>
  )
}
