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
    email: string;
    password: string;
}

export interface UserRegister {
    email: string;
    password: string;
    confirmPassword: string;
}