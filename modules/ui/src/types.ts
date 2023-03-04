export interface User {
    email: string;
    password: string;
    recordings: Recording[];
}

export interface Recording {
    url: string;
    timestamps: number[];
}

export interface UserLogin {
    username: string;
    password: string;
}

export interface UserRegister {
    username: string;
    password: string;
    confirmPassword: string;
}