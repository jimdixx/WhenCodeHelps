import { useState } from "react";
import { Form } from "./components/Form";
import { Navbar } from "./components/Navbar";
import { User } from "./types";
import { AuthForm } from "./components/AuthForm";

function App() {
  const [page, setPage] = useState<"form" | "records">("form");
  const [loggedIn, setLoggedIn] = useState<boolean>(true);
  const [user, setUser] = useState<User>();

  return (
    <>
      <Navbar setPage={setPage} loggedIn={loggedIn} />
      <div className="prose container mx-auto mt-6 text-center">
        <h1>Text to speech app</h1>
        {!!loggedIn ? (
          <>{page === "form" ? <Form /> : <h2>My Recordings</h2>}</>
        ) : (
          <AuthForm />
        )}
      </div>
    </>
  );
}
export default App;
