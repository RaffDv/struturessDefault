const express = require("express");
const sequelize = require("./config/database");
const usersRoutes = require("./routes/User");

const app = express();

app.use(express.json());

app.use("/api", usersRoutes);

const PORT = process.env.PORT || 5000;

sequelize.sync().then(() => {
  app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
});
