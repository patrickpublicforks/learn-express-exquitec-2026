import { generateJwtToken } from "../config/jwt.config.js";
import { User } from "../services/index.js";
import { comparePassword, hashPassword } from "../utils/password-hash.js";

export async  function loginController(req, res) {
  const { email, password } = req.body;

  let user = await User.findOne({ where:  {email : email}, raw: true })

  if (user == null){
    return res.status(400).json({ message: "user doesnt exist"})
  }

  if (!comparePassword(password, user.password)) {
    return res.status(400).json({ message: "invalid email/password" });
  }

  const token = generateJwtToken(user.id)

  res.json({
    message: "success",
    data: { token }
  });
}

export async function signupController(req, res) {
  const { email, password , age, username } = req.body;

  let user = await User.findOne({ where: { email: email } });

  if (user != null){
    return res.status(400).json({ message: "user already exist"})
  }
  const passwordHash = await hashPassword(password)

  user = await User.create({
    email,
    username,
    age,
    password: passwordHash,
  });

  res.json({
    message: "success",
  });
}

export async function profileController(req, res) {
  let user = await User.findOne({ where: { id: req.user_id }, raw: true });
  res.json({
    message: "success",
    data: {...user, password: undefined}
  });
}