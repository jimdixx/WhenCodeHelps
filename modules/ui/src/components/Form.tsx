import { FormEvent, useState } from "react";
import { ErrorAlert } from "./ErrorAlert";
import { SuccessAlert } from "./SuccessAlert";

export const Form = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [errorMsg, setErrorMsg] = useState("");
  const [isSuccess, setIsSuccess] = useState(false);

  const validateFile = () => {
    const MAX_FILE_SIZE = 40960;

    if (!selectedFile) {
      setIsSuccess(false);
      setErrorMsg("No file selected");
      return false;
    }
    const fileSizeKiloBytes = selectedFile.size / 1024;

    if (fileSizeKiloBytes > MAX_FILE_SIZE) {
      setIsSuccess(false);
      setErrorMsg("File size exceeds maximum size of 40mb");
      return false;
    }
    return true;
  };

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (validateFile()) {
      setIsSuccess(true);
      setErrorMsg("");
      console.log({ selectedFile });
    }
  };

  const handleFileInputChange = (event: any) => {
    setSelectedFile(event.target.files[0]);
  };

  return (
    <div className="rounded-lg shadow-lg shadow-black p-4 justify-center text-center">
      <h2 className="mt-0">Upload your file</h2>
      <form className="flex flex-col" onSubmit={handleSubmit}>
        {!!errorMsg && <ErrorAlert message={errorMsg} />}
        {!!isSuccess && <SuccessAlert />}
        <input
          type="file"
          className="file-input file-input-bordered file-input-primary w-full max-w-xs my-4 mx-auto"
          accept="application/epub+zip,text/plain"
          onChange={handleFileInputChange}
        />
        <button className="btn btn-primary px-2">Convert to speech</button>
      </form>
    </div>
  );
};
