import { Login } from "./Login";
import { Register } from "./Register";

export const AuthForm = () => {
  return (
    <div className="rounded-lg shadow-lg shadow-black p-4 justify-center text-center prose grid sm:grid-cols-2">
      <Login />
      <Register />
    </div>
  );
};