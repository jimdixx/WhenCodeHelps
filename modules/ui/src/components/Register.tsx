import { ChangeEvent, useState } from "react";
import { UserRegister } from "../types";
import { loginUser } from "../api/client";

export const Register = () => {
    const [login, setLogin] = useState<UserRegister>({ username: "", password: "", confirmPassword: "" });
  const handleChange = (e: ChangeEvent<any>) => {
    const { name, value } = e.target;
    setLogin((prevInput) => {
      return { ...prevInput, [name]: value };
    });
  };

  const handleLogin = async (e: ChangeEvent<any>) => {
    e.preventDefault();
    if(login.username) await loginUser(login.username)
  }
  return (
    <div>
      <h2 className="mt-0">Create new account</h2>
      <form className="p-2" onSubmit={handleLogin}>
        <input
          type="text"
          name="username"
          placeholder="Username"
          className="input input-bordered input-primary w-full max-w-xs my-2"
          value={login.username}
          onChange={handleChange}
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          className="input input-bordered input-primary w-full max-w-xs my-2"
          value={login.password}
          onChange={handleChange}
        /> 
        
        <input
          type="password"
          name="confirmPassword"
          placeholder="Confirm Password"
          className="input input-bordered input-primary w-full max-w-xs my-2"
          value={login.confirmPassword}
          onChange={handleChange}
        />
        <button className="btn btn-primary" type="submit">Register</button>
      </form>
    </div>
  );
};
