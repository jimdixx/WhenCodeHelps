import { ChangeEvent, useState } from "react";
import { UserLogin } from "../types";

export const Login = () => {
  const [login, setLogin] = useState<UserLogin>({ username: "", password: "" });
  const handleChange = (e: ChangeEvent<any>) => {
    const { name, value } = e.target;
    setLogin((prevInput) => {
      return { ...prevInput, [name]: value };
    });
  };
  return (
    <div className="flex flex-col justify-center">
      <h2 className="mt-0">Login to your account</h2>
      <form className="p-2">
        <input
          type="username"
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
        <button className="btn btn-primary">Login</button>
      </form>
    </div>
  );
};
