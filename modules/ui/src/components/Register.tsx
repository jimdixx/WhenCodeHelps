import { ChangeEvent, useState } from "react";
import { UserRegister } from "../types";

export const Register = () => {
    const [login, setLogin] = useState<UserRegister>({ email: "", password: "", confirmPassword: "" });
  const handleChange = (e: ChangeEvent<any>) => {
    const { name, value } = e.target;
    setLogin((prevInput) => {
      return { ...prevInput, [name]: value };
    });
  };
  return (
    <div>
      <h2 className="mt-0">Create new account</h2>
      <form className="p-2">
        <input
          type="email"
          name="email"
          placeholder="Email"
          className="input input-bordered input-primary w-full max-w-xs my-2"
          value={login.email}
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
        <button className="btn btn-primary">Register</button>
      </form>
    </div>
  );
};
