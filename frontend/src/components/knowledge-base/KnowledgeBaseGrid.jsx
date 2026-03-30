import KnowledgeBaseCard from "./KnowledgeBaseCard";

const KnowledgeBaseGrid = ({ items, onDelete }) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {items.map((item, index) => (
        <KnowledgeBaseCard
          key={item.id || index}
          item={item}
          onDelete={() => onDelete(item.id)}
        />
      ))}
    </div>
  );
};

export default KnowledgeBaseGrid;
