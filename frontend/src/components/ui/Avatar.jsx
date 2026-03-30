const Avatar = ({ initials, className = "" }) => {
  return (
    <div
      className={`w-8 h-8 rounded-full bg-primary/20 border border-primary/50 text-white flex items-center justify-center font-medium text-sm cursor-pointer hover:bg-primary/40 transition-colors ${className}`}
    >
      {initials}
    </div>
  );
};

export default Avatar;
