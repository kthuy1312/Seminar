import { useState, useEffect, useCallback } from "react";
import { postApi } from "../api/apiService";
import { useAuth } from "../context/AuthContext";
import Layout from "../components/common/Layout";
import PostCard from "../components/post/PostCard";
import FloatingActionButton from "../components/common/FloatingActionButton";
import PostingModal from "../components/modal/PostingModal";
import NameInputModal from "../components/modal/NameInputModal";

const HomePage = () => {
  const [posts, setPosts] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");
  const [isPostModalOpen, setIsPostModalOpen] = useState(false);
  const [isNameModalOpen, setIsNameModalOpen] = useState(false);
  const { isAuthenticated, isLoading: authLoading } = useAuth();

  const fetchPosts = useCallback(async () => {
    if (!isAuthenticated) return;

    try {
      setIsLoading(true);
      setError("");
      const response = await postApi.getPosts();
      setPosts(response.data);
    } catch {
      setError("An error occurred while loading posts.");
    } finally {
      setIsLoading(false);
    }
  }, [isAuthenticated]);

  useEffect(() => {
    if (!authLoading && !isAuthenticated) {
      setIsNameModalOpen(true);
    } else if (isAuthenticated) {
      fetchPosts();
    }
  }, [authLoading, isAuthenticated, fetchPosts]);

  return (
    <Layout>
      <div className="w-full max-w-2xl mx-auto">
        <h1 className="text-2xl font-bold mb-6">
          Contoso Outdoor Social
        </h1>
      </div>
    </Layout>
  );
};

export default HomePage;
