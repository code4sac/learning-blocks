import React from 'react';
import styles from './LoadingSkeleton.module.css';

const LoadingSkeleton = () => {
    return (
        <div className={styles.skeletonContainer}>
            <div className={styles.skeletonHeader}></div>
            <div className={styles.skeletonBody}></div>
            <div className={styles.skeletonFooter}></div>
        </div>
    );
};

export default LoadingSkeleton;