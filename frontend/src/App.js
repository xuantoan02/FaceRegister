

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Register from "./Register";
import Login from "./Login"
import UploadAvatar from "./component/UploadAvt"





const App = () => {
  return (
    <Router>
      <Switch>

        <Route path="/Login" component={Login} />
        <Route path="/Register" component={Register} />
        <Route path="/upload-avt" component={UploadAvatar} />
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





