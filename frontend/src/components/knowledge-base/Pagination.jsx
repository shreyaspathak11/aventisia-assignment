import {
  ChevronLeft,
  ChevronRight,
  ChevronsLeft,
  ChevronsRight,
  ChevronDown,
} from "lucide-react";

const Pagination = ({ totalRows = 6 }) => {
  return (
    <div className="flex items-center justify-between text-sm text-gray-800 font-medium">
      <div>
        {totalRows} rows{totalRows !== 1 ? "(s)" : ""}
      </div>

      <div className="flex items-center gap-8">
        <div className="flex items-center gap-3">
          <span>Rows per page</span>
          <div className="relative">
            <select className="appearance-none bg-white border border-gray-200 rounded-md py-1.5 pl-3 pr-8 focus:outline-none focus:ring-1 focus:ring-primary shadow-sm hover:border-gray-300 transition-colors cursor-pointer">
              <option>10</option>
              <option>20</option>
              <option>50</option>
            </select>
            <ChevronDown className="absolute right-2 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-500 pointer-events-none" />
          </div>
        </div>

        <div className="flex items-center gap-4">
          <span>page 1 of 1</span>

          <div className="flex items-center gap-1">
            <button
              className="p-1.5 rounded-md border border-gray-200 text-gray-400 hover:text-gray-600 hover:bg-gray-50 transition-colors disabled:opacity-50"
              disabled
            >
              <ChevronsLeft className="w-4 h-4" />
            </button>
            <button
              className="p-1.5 rounded-md border border-gray-200 text-gray-400 hover:text-gray-600 hover:bg-gray-50 transition-colors disabled:opacity-50"
              disabled
            >
              <ChevronLeft className="w-4 h-4" />
            </button>
            <button
              className="p-1.5 rounded-md border border-gray-200 text-gray-400 hover:text-gray-600 hover:bg-gray-50 transition-colors disabled:opacity-50"
              disabled
            >
              <ChevronRight className="w-4 h-4" />
            </button>
            <button
              className="p-1.5 rounded-md border border-gray-200 text-gray-400 hover:text-gray-600 hover:bg-gray-50 transition-colors disabled:opacity-50"
              disabled
            >
              <ChevronsRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Pagination;
