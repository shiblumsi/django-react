import React, { useState } from "react";

export default function Question() {
  const [opts, setOpt] = useState([""])
  const [qus, setQus] = useState('')
  const [ans, setAns] = useState('');
  const handleAdd = ()=>{
    
    setOpt([...opts, ""])
   
  }
  const handleRemove = (index) => {
    const newOpts = opts.filter((_, i)=> i !== index)
    setOpt(newOpts)
    
  }

  const handleOptionChange = (index, value) => {
    
    const newOpts = [...opts]
    newOpts[index] = value
    setOpt(newOpts)
    
  };

  const handleSubmit = ()=>{
    console.log(opts);
    console.log(qus);
    console.log(ans);
  }
  


  return (
    <div>
      <input
        className="form-control"
        type="text"
        placeholder="enter your question"
        value={qus}
        onChange={(e) => setQus(e.target.value)}
      /><br/>
      <input
        className="form-control"
        type="text"
        placeholder="enter your answer"
        value={ans}
        onChange={(e) => setAns(e.target.value)}
      /><br/>
      {opts.map((opt, index) => (
        <>
          <input
            key={index}
            type="text"
            value={opt}
            placeholder={`Option ${index + 1}`}
            onChange={(e) => handleOptionChange(index, e.target.value)}
          />{" "}
          <span></span>
          <button
            className="btn btn-sm btn-danger"
            onClick={() => handleRemove(index)}
          >
            Remove
          </button>
          <br />
          <br />
        </>
      ))}

      <button onClick={handleAdd}>Add Option</button>
      <button onClick={handleSubmit}>submit</button>
    </div>
  );
}
