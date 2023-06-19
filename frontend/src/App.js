

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Register from "./component/register/Signup";
// import Login from "./component/Login"





const App = () => {
  return (
    <Router>
      <Switch>

        {/* <Route path="/Login" component={Login} /> */}
        <Route path="/Register" component={Register} />
      </Switch>
    </Router>
  );
};

export default App;




// const App1 = () => {
//   const [email, setEmail] = useState("")
//   const [password, setPassword] = useState("")
  
// const login = () => {
//   console.log("Info:", email, password)
// }
//   return (
//     <div>
//       <App2/>
//       <input value={email} onChange={(e) => {setEmail(e.target.value)}} />
//       <input value={password} onChange={(e) => {setPassword(e.target.value)}} />

// <button onClick={login}>Login</button>
//       {email}
//       {password}
//     </div>
//   )
// }
// export default App1;





