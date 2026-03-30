import { NavLink } from "react-router-dom";
import { menuSections } from "../../data/menuData";

const Sidebar = () => {
  return (
    <aside className="w-[280px] bg-white border-r border-gray-100/50 h-[calc(100vh-64px)] fixed left-0 top-[64px] overflow-y-auto z-40">
      <nav className="py-8 px-5 space-y-10">
        {menuSections.map((section, index) => (
          <div key={index}>
            <h3 className="text-[11px] font-bold text-gray-400 mb-4 px-3 uppercase tracking-widest">
              {section.title}
            </h3>
            <ul className="space-y-1.5">
              {section.items.map((item, itemIdx) => (
                <li key={itemIdx}>
                  <NavLink
                    to={item.path}
                    className={({ isActive }) => `
                      relative flex items-center gap-3 px-3 py-2 rounded-lg text-[13px] font-medium transition-all
                      ${
                        isActive
                          ? "bg-primary/5 text-primary"
                          : "text-gray-500 hover:bg-gray-50 hover:text-gray-900"
                      }
                    `}
                  >
                    {({ isActive }) => (
                      <>
                        {item.name === "Knowledge Base" && isActive && (
                          // Just for the sake of the assignment, ensure Knowledge Base has the active indicator line
                          <div
                            className="absolute left-0 w-1 h-7 bg-primary rounded-r-full shadow-sm"
                            style={{ left: "-20px" }}
                          ></div>
                        )}
                        <span
                          className={
                            isActive
                              ? "text-primary border-primary"
                              : "text-gray-400"
                          }
                        >
                          {item.icon}
                        </span>
                        {item.name}
                      </>
                    )}
                  </NavLink>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </nav>
    </aside>
  );
};

export default Sidebar;
