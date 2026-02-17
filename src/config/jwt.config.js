import jwt from "jsonwebtoken"

export function generateJwtToken(user_id){
    return jwt.sign({ user_id }, process.env.JWT_SECRET, {
      expiresIn: process.env.JWT_EXPIRY,
    });
}

export function verifyJwtToken(token){
    return jwt.verify(token, process.env.JWT_SECRET);
}