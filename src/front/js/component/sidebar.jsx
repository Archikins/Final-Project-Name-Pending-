import React, { useState } from "react"; // you were missing the useState
import {
  FaTh,
  FaUserAlt,
  FaHeart,
  FaSearch,
  FaBars,
  FaSignOutAlt,
} from "react-icons/fa";
import { NavLink } from "react-router-dom";
import Logo from "../../img/rigo-baby.jpg";
import { Logout } from "./logout";

const Sidebar = ({ children }) => {
  const [isOpen, setIsOpen] = useState(false);
  const toggle = () => setIsOpen(!isOpen);
  const menuItem = [
    {
      path: "/",
      name: "Dashboard",
      icon: <FaTh />,
    },
    {
      path: "/account",
      name: "Account",
      icon: <FaUserAlt />,
    },
    {
      path: "/recipesearch",
      name: "Search",
      icon: <FaSearch />,
    },

    {
      path: "/favorites",
      name: "Favorites",
      icon: <FaHeart />,
    },

    {
      path: "/logout",
      name: "Log Out",
      icon: <FaSignOutAlt />,
    },
  ];
  return (
    <div className="container">
      <div style={{ width: isOpen ? "300px" : "50px" }} className="sidebar">
        <div className="top_section">
          <div className="logo_name">
            <img className="logo" src={Logo} />
            <h1
              style={{ display: isOpen ? "block" : "none" }}
              className="appname"
            >
              Name
            </h1>
          </div>
          <div style={{ marginLeft: isOpen ? "0px" : "0px" }} className="bars">
            <FaBars onClick={toggle} />
          </div>
          {menuItem.map((item, index) => (
            <NavLink
              to={item.path}
              key={index}
              className="link"
              activeclassName="active"
            >
              <div className="icon">{item.icon}</div>
              <div
                style={{ display: isOpen ? "block" : "none" }}
                className="link_text"
              >
                {item.name}
              </div>
            </NavLink>
          ))}
        </div>
      </div>
      <main>{children}</main>
    </div>
  );
};

export default Sidebar;