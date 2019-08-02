import axios from "axios";

function login(username, password) {
    const payload = {
        username: username,
        password: password,
    };

    return axios({
        method: "post",
        url: "/login",
        data: payload,
    });
}

function logout() {
    const payload = {
        jwt: localStorage.getItem("t"),
    };

    return axios({
        method: "post",
        url: "/logout",
        data: payload,
    });
}

export const userService = {
    login,
    logout,
};
