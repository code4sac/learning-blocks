export async function fetchAuth() {
    //let user = new User();
    //user.id = '0000000001';
    //user.name = '001';
    //let result = { isAuthenticated: true,  user };
    let userId = localStorage.getItem("userId");
    return userId ? {isAuthenticated: true, user: {id: userId}} : {isAuthenticated: false, user: undefined};
}