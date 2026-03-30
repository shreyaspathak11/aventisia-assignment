const Button = ({
  children,
  variant = "primary",
  icon,
  className = "",
  ...props
}) => {
  const baseStyle =
    "flex items-center justify-center gap-2 rounded-md font-medium transition-all active:scale-95 disabled:opacity-70 disabled:pointer-events-none";

  const variants = {
    primary:
      "bg-primary text-white hover:bg-primary/90 px-4 py-2 text-sm shadow-sm",
    secondary:
      "bg-white text-gray-700 border border-gray-200 hover:bg-gray-50 px-4 py-2 text-sm shadow-sm",
    ghost:
      "text-gray-500 hover:text-gray-700 hover:bg-gray-100 p-1.5 rounded-md",
  };

  return (
    <button
      className={`${baseStyle} ${variants[variant]} ${className}`}
      {...props}
    >
      {icon && icon}
      {children}
    </button>
  );
};

export default Button;
