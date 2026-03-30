import { Search } from "lucide-react";

const SearchBox = ({
  wrapperClass = "",
  inputClass = "",
  placeholder = "Search...",
  shortcut,
  iconProps = {},
}) => {
  return (
    <div className={`relative group ${wrapperClass}`}>
      <Search
        className={`absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400 group-focus-within:text-primary transition-colors pointer-events-none ${iconProps.className || ""}`}
      />
      <input
        type="text"
        placeholder={placeholder}
        className={`w-full text-sm rounded-md pl-10 focus:outline-none focus:ring-1 focus:ring-primary transition-all ${inputClass}`}
      />
      {shortcut && (
        <div className="absolute right-3 top-1/2 -translate-y-1/2 flex items-center pointer-events-none">
          <span className="text-xs bg-black/20 text-gray-400 px-1.5 py-0.5 rounded border border-white/10">
            {shortcut}
          </span>
        </div>
      )}
    </div>
  );
};

export default SearchBox;
