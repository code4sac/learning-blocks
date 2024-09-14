import React from 'react'

import styles from './LoadingSkeleton.module.css'

const LoadingSkeleton = () => {
  return (
    <div className={styles.skeletonContainer}>
      <div className={styles.skeletonHeader} />
      <div className={styles.skeletonBody} />
      <div className={styles.skeletonFooter} />
    </div>
  )
}

export default LoadingSkeleton
