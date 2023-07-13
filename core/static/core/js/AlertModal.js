import { useModal } from "/static/core/js/PageLayout.js";

const [alertModal, openAlertModal, closeAlertModal] = useModal(
  "alert-modal",
  null,
  "close-alert-modal-button"
);

if (alertModal) {
  openAlertModal();
}
