import { useState } from "react";
import { Form } from "./components/Form";
import { Navbar } from "./components/Navbar";
import { User } from "./types";
import { AuthForm } from "./components/AuthForm";
import { RecordsList } from "./components/RecordsList";

function App() {
  const [page, setPage] = useState<"form" | "records">("form");
  const [loggedIn, setLoggedIn] = useState<boolean>(false);
  const [user, setUser] = useState<User>();
  const [loading, setLoading] = useState<boolean>(false);

  return (
    <>
      <Navbar setPage={setPage} loggedIn={loggedIn} />
      <div className="prose container mx-auto mt-6 text-center">
        <h1>Text to speech app</h1>
        {!!loggedIn ? (
          <>{page === "form" ? <Form /> : <RecordsList />}</>
        ) : (
          <AuthForm />
        )}
      </div>
    </>
  );
}
export default App;
