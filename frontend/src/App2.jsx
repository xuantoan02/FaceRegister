const App2 = () => {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    
  const login = () => {
    console.log("Info:", email, password)
  }
    return (
      <div>
        <input value={email} onChange={(e) => {setEmail(e.target.value)}} />
        <input value={password} onChange={(e) => {setPassword(e.target.value)}} />
  
  <button onClick={login}>Login</button>
        {email}
        {password}
      </div>
    )
  }

  export default App2