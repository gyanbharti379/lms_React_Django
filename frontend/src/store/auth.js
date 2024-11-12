import {create} from 'zustand';
import {mountStoreDevtool} from 'simple-zustand-devtools';

const useAuthStore = create((set,get) => ({
    allUserData: null,
    loading: false,
    
    user:() =>({
            user_email: get().allUserData?.email || null,
            user_full_name: get().allUserData?.full_name || null,
            
    }),
    setUser: (user) => set({allUserData: user}),

    setLoading: (loading) => set({loading: loading}),
    // isLoggedIn: () => get().allUserData,

   

    isAuthenticated: false,
    login: () => set({isAuthenticated: true}),
    logout: () => set({isAuthenticated: false}),
}));

if (process.env.NODE_ENV !== 'production') {
    mountStoreDevtool('Auth', useAuthStore);
}

export default useAuthStore