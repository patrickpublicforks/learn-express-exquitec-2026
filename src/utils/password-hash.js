import bcrypt from "bcrypt";

const saltRounds = 10;

export async function hashPassword(plainPassword) {
  const hashedPassword = await bcrypt.hash(plainPassword, saltRounds);
  // Store the 'hashedPassword' in your database
  return hashedPassword;
}

export async function comparePassword(plainPassword, hashPassword) {
  const match = await bcrypt.compare(plainPassword, hashPassword);
  // Store the 'hashedPassword' in your database
  return match;
}