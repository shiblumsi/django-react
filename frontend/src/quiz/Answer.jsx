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
        
    </div>
  )
}
