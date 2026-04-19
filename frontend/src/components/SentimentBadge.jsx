const colors = {
  positive: "bg-green-100 text-green-800",
  neutral: "bg-gray-100 text-gray-700",
  negative: "bg-red-100 text-red-800",
};

export default function SentimentBadge({ sentiment }) {
  return (
    <span
      className={`text-xs font-medium px-2 py-0.5 rounded-full ${
        colors[sentiment] || colors.neutral
      }`}
    >
      {sentiment || "neutral"}
    </span>
  );
}