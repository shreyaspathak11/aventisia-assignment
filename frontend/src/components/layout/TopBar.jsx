import { Bell, ChevronDown } from "lucide-react";
import SearchBox from "../ui/SearchBox";
import Avatar from "../ui/Avatar";

const TopBar = () => {
  return (
    <header className="h-[64px] bg-secondary flex items-center justify-between px-6 shrink-0 w-full fixed top-0 z-50 shadow-md">
      <div className="flex items-center gap-6">
        {/* Logo Area */}
        <div className="flex items-center gap-2">
          <div className="w-7 h-7 bg-primary rounded flex items-center justify-center">
            {/* Simple logo approximation */}
            <span className="text-white font-bold text-base leading-none transform -translate-y-px">
              △
            </span>
          </div>
          <span className="text-white font-semibold text-base tracking-wide">
            Worcspace
          </span>
        </div>

        {/* Workspace Selector */}
        <button className="flex items-center gap-2 bg-white/10 hover:bg-white/20 px-3 py-1.5 rounded-md text-[13px] text-gray-200 transition-colors">
          <span>Worcspace 1</span>
          <ChevronDown className="w-4 h-4 text-gray-400" />
        </button>
      </div>

      {/* Global Search */}
      <div className="flex-1 max-w-[500px] mx-8">
        <SearchBox
          placeholder="Search..."
          shortcut="⌘K"
          inputClass="bg-white/10 text-white placeholder-gray-400 border-none focus:bg-white/15 py-2 rounded-full shadow-inner"
          iconProps={{ className: "text-gray-400 ml-1" }}
        />
      </div>

      {/* Right Icons */}
      <div className="flex items-center gap-5">
        <button className="relative text-gray-400 hover:text-white transition-colors">
          <Bell className="w-5 h-5" />
          <span className="absolute top-0 right-0 w-2 h-2 bg-white rounded-full border-2 border-secondary"></span>
        </button>
        <Avatar initials="GK" />
      </div>
    </header>
  );
};

export default TopBar;
