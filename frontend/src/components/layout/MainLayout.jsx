import TopBar from "./TopBar";
import Sidebar from "./Sidebar";
import { Outlet } from "react-router-dom";

const MainLayout = () => {
  return (
    <div className="min-h-screen flex flex-col bg-[#F9FAFB] font-sans text-gray-800 selection:bg-primary/20">
      <TopBar />
      <div className="flex flex-1 pt-[64px] overflow-hidden">
        <Sidebar />
        <main className="flex-1 ml-[280px] px-8 py-6 min-h-[calc(100vh-64px)] overflow-y-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default MainLayout;
