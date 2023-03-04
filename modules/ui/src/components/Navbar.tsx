import { Dispatch, SetStateAction } from "react";

export const Navbar = (props: {
  setPage: Dispatch<SetStateAction<"form" | "records">>;
  loggedIn: boolean;
}) => {
  const { setPage, loggedIn } = props;

  const handleLogout = () => {
    console.log("Logging out");
  };

  return (
    <div className="navbar bg-base-100">
      <div className="navbar-start">
        {!!loggedIn && (
          <div className="dropdown">
            <label tabIndex={0} className="btn btn-ghost lg:hidden">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M4 6h16M4 12h8m-8 6h16"
                />
              </svg>
            </label>
            <ul
              tabIndex={0}
              className="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52"
            >
              <li>
                <a onClick={() => setPage("form")}>New recording</a>
              </li>
              <li>
                <a onClick={() => setPage("records")}>My recordings</a>
              </li>
            </ul>
          </div>
        )}

        <a className="btn btn-ghost normal-case text-xl">Text 2 Speech</a>
      </div>
      <div className="navbar-center hidden lg:flex">
        {!!loggedIn && (
          <ul className="menu menu-horizontal px-1">
            <li>
              <a onClick={() => setPage("form")}>New recording</a>
            </li>
            <li>
              <a onClick={() => setPage("records")}>My recordings</a>
            </li>
          </ul>
        )}
      </div>
      <div className="navbar-end">
        {!!loggedIn && (
          <a className="btn btn-error" onClick={handleLogout}>
            Logout
          </a>
        )}
      </div>
    </div>
  );
};
